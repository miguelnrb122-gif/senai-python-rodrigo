import ast, contextlib, io, json, math

class BoundedOutput(io.StringIO):
    def write(self, s):
        if self.tell() + len(s) > 12000:
            raise RuntimeError('A saída ficou muito grande. Reduza a quantidade de impressões.')
        return super().write(s)

def grade_student(code, task):
    checks = []
    def check(ok, text):
        checks.append({'ok': bool(ok), 'text': text})
    output = BoundedOutput()
    env = {'__name__': '__student__'}
    try:
        tree = ast.parse(code)
        with contextlib.redirect_stdout(output):
            exec(compile(tree, '<seu_codigo>', 'exec'), env)
    except Exception as e:
        line = getattr(e, 'lineno', None)
        if line is None:
            import traceback
            for f in traceback.extract_tb(e.__traceback__):
                if f.filename == '<seu_codigo>': line = f.lineno
        tips = {'SyntaxError': 'Confira aspas, parênteses, colchetes e dois-pontos.', 'NameError': 'Confira o nome da variável e crie-a antes de usar.', 'KeyError': 'Confira se a chave existe e se o texto está escrito exatamente igual.', 'TypeError': 'Confira os tipos dos valores e a forma de chamar a instrução.', 'IndentationError': 'Confira os espaços no começo da linha.'}
        return json.dumps({'passed': False, 'output': output.getvalue(), 'error': f'{type(e).__name__}' + (f' na linha {line}' if line else '') + f': {e}\n' + tips.get(type(e).__name__, 'Leia a mensagem e revise a instrução indicada.'), 'checks': []}, ensure_ascii=False)
    lines = [l.strip() for l in output.getvalue().strip().splitlines()]
    def dictionary_line(i, expected):
        try: return ast.literal_eval(lines[i]) == expected
        except Exception: return False
    def number_line(i, expected):
        try: return math.isclose(float(lines[i]), expected, abs_tol=1e-8)
        except Exception: return False
    def approx(value, expected):
        return type(value) in (int, float) and math.isclose(value, expected, abs_tol=1e-8)
    def has_access(var, key):
        return any(isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id == var and isinstance(n.slice, ast.Constant) and n.slice.value == key for n in ast.walk(tree))
    def has_update(var, key, value):
        return any(isinstance(n, ast.Assign) and any(isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name) and t.value.id == var and isinstance(t.slice, ast.Constant) and t.slice.value == key for t in n.targets) for n in ast.walk(tree))
    def has_initial(var, key, value):
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id == var for t in n.targets) and isinstance(n.value,ast.Dict):
                try:
                    if approx(ast.literal_eval(n.value).get(key), value): return True
                except Exception: pass
        return False
    if task == 0:
        check(lines == ['Olá, turma!'], 'Mostrar exatamente Olá, turma! na tela.')
    elif task == 1:
        check(type(env.get('produto')) is str and env.get('produto') == 'Arroz', 'produto é o texto Arroz (str).')
        check(type(env.get('preco')) is float and approx(env.get('preco'),25.9), 'preco é o decimal 25.90 (float).')
        check(type(env.get('quantidade')) is int and env.get('quantidade') == 2, 'quantidade é o inteiro 2 (int).')
        check(type(env.get('disponivel')) is bool and env.get('disponivel') is True, 'disponivel é True (bool).')
        check(lines == ['Arroz', "<class 'float'>", "<class 'int'>", "<class 'bool'>"], 'Mostrar produto e os três tipos, um por linha, na ordem solicitada.')
    elif task == 2:
        expected=['Arroz','Feijão','Leite','Café']
        check(type(env.get('carrinho')) is list and env['carrinho']==expected, 'carrinho contém os quatro produtos na ordem pedida.')
        check(any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='append' and isinstance(n.func.value,ast.Name) and n.func.value.id=='carrinho' for n in ast.walk(tree)), 'Usar append() para acrescentar Café.')
        check(has_access('carrinho',0), 'Acessar o primeiro produto com carrinho[0].')
        check(len(lines)==2 and lines[0]=='Arroz' and dictionary_line(1,expected), 'Mostrar Arroz e depois a lista completa, em duas linhas.')
    elif task in (3,4):
        expected={'Arroz':25.9,'Feijão':8.5,'Leite':5.9 if task==3 else 6.2}
        check(type(env.get('produtos')) is dict and env['produtos']==expected, 'Manter produtos e preços conforme o pedido.')
        check(has_access('produtos','Leite'), 'Consultar o preço usando a chave Leite.')
        if task==4:
            check(has_initial('produtos','Leite',5.9), 'Manter o dicionário inicial com Leite a 5.90.')
            check(has_update('produtos','Leite',6.2), 'Atualizar diretamente a chave Leite.')
        check(len(lines)==1 and number_line(0,expected['Leite']), 'Mostrar somente o preço solicitado.')
    elif task==5:
        initial={'Chocolate':6.5,'Refrigerante':8.,'Pipoca':5.5}
        final={**initial,'Pipoca':4.5}
        check(type(env.get('mercado')) is dict and env['mercado']==final, 'mercado termina com os três produtos e Pipoca a 4.50.')
        check(has_access('mercado','Pipoca') and has_update('mercado','Pipoca',4.5), 'Consultar e atualizar a chave Pipoca.')
        check(len(lines)==3 and dictionary_line(0,initial), 'Primeira linha: mostrar o mercado antes da alteração.')
        check(len(lines)>=2 and number_line(1,5.5), 'Segunda linha: mostrar o preço inicial da Pipoca, 5.50.')
        check(len(lines)==3 and dictionary_line(2,final), 'Terceira linha: mostrar o mercado atualizado.')
    return json.dumps({'passed': all(c['ok'] for c in checks), 'output': output.getvalue(), 'checks': checks}, ensure_ascii=False)
