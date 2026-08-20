function updateQuantity(code, amount) {
  const product = products.find((item) => item.code === code);

  if (!product) {
    console.log("ไม่พบสินค้า");
    return false;
  }

  if (typeof amount !== "number" || Number.isNaN(amount)) {
    console.log("จำนวนต้องเป็นตัวเลข");
    return false;
  }

  if (product.quantity + amount < 0) {
    console.log("จำนวนคงเหลือไม่พอ");
    return false;
  }

  product.quantity += amount;
  saveProducts();
  console.log("อัปเดตจำนวนสินค้าสำเร็จ");
  return true;
}