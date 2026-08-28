# Money Exchange System

This document covers the database design for Money Exchange System using the ER diagram and the justification for each table. 

## Entity-Relationship Diagram

```mermaid
erDiagram
  ADMINS ||--o{ USERS : "registers (optional)"
  ADMINS ||--o{ TRANSACTIONS : processes
  ADMINS ||--o{ VERIFICATION_DOCUMENTS : requests
  USERS ||--o{ TRANSACTIONS : requests
  USERS ||--o{ CARDS : owns
  USERS ||--o{ VERIFICATION_DOCUMENTS : submits
  CARDS ||--o{ TRANSACTIONS : funds
  CURRENCIES ||--o{ EXCHANGE_RATES : base
  CURRENCIES ||--o{ EXCHANGE_RATES : target
  CURRENCIES ||--o{ TRANSACTIONS : "sold currency"
  CURRENCIES ||--o{ TRANSACTIONS : "bought currency"

  ADMINS {
    int admin_id PK
    string username
    string password_hash
    string full_name
    string role
  }
  USERS {
    int user_id PK
    string username
    string password_hash
    string first_name
    string last_name
    string email
    string status
    int registered_by FK
  }
  CARDS {
    int card_id PK
    int user_id FK
    string cardholder_name
    string card_last4
    string expiry_date
  }
  CURRENCIES {
    string currency_code PK
    string currency_name
    string symbol
  }
  EXCHANGE_RATES {
    int rate_id PK
    string base_currency FK
    string target_currency FK
    real rate
    datetime effective_date
  }
  TRANSACTIONS {
    int transaction_id PK
    int user_id FK
    int card_id FK
    int admin_id FK
    string from_currency FK
    string to_currency FK
    real amount_from
    real amount_to
    string status
    datetime requested_at
  }
  VERIFICATION_DOCUMENTS {
    int document_id PK
    int user_id FK
    int requested_by FK
    string document_type
    string status
  }
```

| Table | Reason |
|---|---|
| `users` | Users log in themselves (View/Update Profile, Change Password use cases)|
| `admins` | staff who manage the platform |
| `cards` |  Required by the mandatory `«include»` from Request Exchange Money → Add Card Information; a user can have multiple cards, so it's its own table|
| `currencies` |  controlled lookup of tradeable currencies |
| `exchange_rates` | Rate history; now read by **View Exchange Rate** and maintained via **Manage Currencies** |
| `transactions` | request lifecycle (pending → approved/rejected) per **Process Exchange Request** |
| `verification_documents` | Required by the optional `«extend»` from Register Account → Request Additional Document; only populated when an admin actually asks for more documents |

## 6. Relationship summary

- One **admin** may manage many **users** (optional — `registered_by` can be `NULL`)
- One **admin** processes many **transactions**; one **admin** may request many **verification documents**
- One **user** makes many **transactions**, owns many **cards**, and may submit many **verification documents**
- One **card** can fund many **transactions**
- One **currency** can be the base or target of many **exchange rates**, and the sold or bought currency in many **transactions**
