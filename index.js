const fs = require("fs");

let products = [];

function saveProducts() {
  fs.writeFileSync("products.json", JSON.stringify(products, null, 2));
}

function addProduct(code, name, quantity) {
  const duplicate = products.some(product => product.code === code);

  if (duplicate) {
    console.log("สินค้านี้มีอยู่แล้ว");
    return;
  }

  products.push({ code, name, quantity });
  saveProducts();
  console.log("เพิ่มสินค้าใหม่สำเร็จ");
}

addProduct("P001", "ดินสอ", 10);