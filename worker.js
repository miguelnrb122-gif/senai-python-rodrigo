const BASE='https://cdn.jsdelivr.net/pyodide/v0.29.2/full/';
let py;
async function init(){try{importScripts(BASE+'pyodide.js');py=await loadPyodide({indexURL:BASE});const r=await fetch('checks.py');if(!r.ok)throw Error('Falha ao carregar a correção.');py.runPython(await r.text());postMessage({type:'ready'})}catch(e){postMessage({type:'init-error',error:String(e)})}}
onmessage=async({data})=>{if(data.type==='init'){await init();return}if(data.type==='run'){try{const fn=py.globals.get('grade_student');const r=fn(data.code,data.task);fn.destroy();postMessage({type:'result',task:data.task,result:JSON.parse(r)})}catch(e){postMessage({type:'result',task:data.task,result:{passed:false,error:String(e),output:'',checks:[]}})}}};
