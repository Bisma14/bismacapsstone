# bismacapsstone
## HALO


```mermaid
graph TD
    A((Start)) --> B[Login Menu]
    B --> C[Enter Username and Password]
    C --> D{Login Successful?}
    D -- Yes --> E[Main Menu]
    D -- No --> B

    E --> F{Choose a Feature}
    F -- Feature 1 --> G[Execute Feature 1]
    F -- Feature 2 --> H[Execute Feature 2]
    F -- Feature 3 --> I[Execute Feature 3]
    F -- Feature 4 --> J[Execute Feature 4]
    F -- Feature 5 --> K[Execute Feature 5]

    G --> L((Return to Main Menu))
    H --> L
    I --> L
    J --> L
    K --> L

    L --> E
