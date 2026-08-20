const fs = require("fs");

function saveProducts(products) {
  fs.writeFileSync("products.json", JSON.stringify(products, null, 2));
}