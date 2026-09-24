sequenceDiagram
    actor Employee as พนักงานคลังสินค้า
    participant Service as InventoryService
    participant Prod as Product
    participant Notif as Notifier (Observer)
    
    Employee->>Service: issue_product("สายไฟ", 8)
    activate Service
    Service->>Prod: ลดจำนวน quantity
    Service->>Service: ตรวจสอบ quantity < threshold
    alt สต็อกต่ำกว่า threshold
        Service->>Service: _notify_managers("สต็อกต่ำ...")
        loop ทุกๆ Notifier ใน list
            Service->>Notif: send("สต็อกต่ำ...")
            activate Notif
            Notif-->>Service: (จำลองพิมพ์ข้อความออกจอ)
            deactivate Notif
        end
    end
    Service-->>Employee: return True
    deactivate Service