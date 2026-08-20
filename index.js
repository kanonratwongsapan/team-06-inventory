const products = [
  { code: "P001", name: "ดินสอ", quantity: 10 }
];

function addProduct(code, name, quantity) {
  const duplicate = products.some(product => product.code === code);

  if (duplicate) {
    console.log("สินค้านี้มีอยู่แล้ว");
    return;
  }

  products.push({ code, name, quantity });
  console.log("เพิ่มสินค้าใหม่สำเร็จ");
}