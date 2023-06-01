const express = require('express');
const app = express();

// Set to public port
const PORT = 4000

app.use(express.static("/home/node/frontend"));

app.get("/youwillneverbruteforcethisapi", (req, res) => {
    res.setHeader("Flag","=[PVS1,(I>HYtWAFC/!%9f$.#0Q&gV@P_A&1ilf,Cb[k-CboEPDDQ\\");
    res.send("BREACH DETECTED. FLAG HAS BEEN HIDDEN. BIG BROTHER IS WATCHING.")
});

app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});
