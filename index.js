function updateQuantity(code, amount) {
  const product = products.find((item) => item.code === code);

  if (!product) {
    console.log("ไม่พบสินค้า");
    return;
  }

  if (product.quantity + amount < 0) {
    console.log("จำนวนคงเหลือไม่พอ");
    return;
  }

  product.quantity += amount;
  saveProducts();
  console.log("อัปเดตจำนวนสินค้าสำเร็จ");
}