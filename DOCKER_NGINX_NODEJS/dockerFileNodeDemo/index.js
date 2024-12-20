const express = require('express');
const app = express();
const port =8000

app.get('/',(req,res)=>{
    res.send("hello world dockerfile!!!!")
});

app.listen(port,() =>{
    console.log(`Exemple app listening at http://localhost:${port}`)
});