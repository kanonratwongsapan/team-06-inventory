classDiagram
    class Product {
        +String name
        +String category
        +Float price
        +Int quantity
        +Int threshold
    }
    
    class Notifier {
        <<Protocol>>
        +send(message: str) None
    }
    
    class EmailNotifier {
        +String email
        +send(message: str) None
    }
    
    class SMSNotifier {
        +String phone
        +send(message: str) None
    }
    
    class NotifierFactory {
        +create(channel: str, config: str) Notifier$
    }
    
    class InventoryService {
        -Dict products
        -List notifiers
        +add_product(product: Product) None
        +issue_product(name: str, qty: int) bool
        +get_inventory_value_by_category() Dict
        -_notify_managers(message: str) None
    }
    
    Notifier <|.. EmailNotifier : Realization
    Notifier <|.. SMSNotifier : Realization
    NotifierFactory ..> Notifier : Dependency
    InventoryService --> Notifier : Composition
    InventoryService --> Product : Composition