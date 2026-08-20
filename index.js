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
    console.log("สินค้านี้มีอยู่แล้ว");
    return;
  }

  products.push({ code, name, quantity });
  saveProducts();
  console.log("เพิ่มสินค้าใหม่สำเร็จ");
}

// test
addProduct("P002", "ยางลบ", 3);
addProduct("P001", "ปากกา", 5);