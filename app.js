const express = require("express"),
  app = express(),
  bodyParser = require("body-parser"),
  PORT = process.env.PORT || 5000,
  got = require("got"),
  Request = require("request");
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  //   res.render("home");
  Request.get(
    "http://api.open-notify.org/iss-now.json",
    (error, response, body) => {
      if (error) {
        return console.dir(error);
      }
      data = JSON.parse(body);
      console.log(data);
      res.render("home", { data: data });
    }
  );
});

app.listen(PORT, function() {
  console.log(`listening to port:${PORT}`);
});
