const fs = require("fs");

let products = [];

if (fs.existsSync("products.json")) {
  const rawData = fs.readFileSync("products.json", "utf8");
  products = JSON.parse(rawData);
}

function saveProducts() {
  fs.writeFileSync("products.json", JSON.stringify(products, null, 2));
}

function addProduct(code, name, quantity) {
  const duplicate = products.some((product) => product.code === code);

  if (duplicate) {
    console.log("Product already exists");
    return;
  }

  products.push({ code, name, quantity });
  saveProducts();
  console.log("Product added successfully");
}

addProduct("P001", "Pencil", 10);