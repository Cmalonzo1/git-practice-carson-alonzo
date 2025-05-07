# Pokemon Card Storage Web Application Diagram

#### User Roles:
- Users should be able to:
    - View All Pokemon Cards
    - Submit new cards (pending admin approval)
    - Assemble and mange decks

- Admins should be able to:
    - Approve user-submitted cards
    - Add new cards
    - Modify and delete existing cards

- Core features:
    - Card Database: Store Pokémon cards with relevant stats
    - Deck Management: Users can create, edit, and remove decks
    - Role-Based Permissions: Admins can manage cards, users can only submit or assemble decks
    - Approval System: New cards require admin approval before being visible



```mermaid
    
    flowchart LR

    classDef blue fill:#0000FF,stroke:#333,stroke-width:2px,color:#000
    classDef orange fill:#FF9500,stroke:#333,stroke-width:2px,color:#000
    classDef green fill:#00FF00,stroke:#333,stroke-width:2px,color:#000
    classDef red fill:#FF0000,stroke:#333,stroke-width:2px,color:#000

    User[User]
    User --o LoginScreen(Login/Register) -- Is Normal User -->Homepage{Homepage}:::blue
    LoginScreen -- Is Admin User --> AdminHomepage{Admin Homepage}:::orange

     Homepage -.-> CardSection[View Cards]
            CardSection -- Filters --> Filters((Type, Ability, Generation, Region, Rarity))
            CardSection --> SubmitNewCard[Submit New Card]
                SubmitNewCard -->|Admin Review| Approval{Approved?}
                    Approval -- Yes --> AdminAction[Add Card to Database]:::green --> CardAccepted(Card Accepted)
                    Approval -- No --> CardRejected(Card Rejected):::red
        
        Homepage -.-> ViewDecks[View Decks]
            ViewDecks -.-> NewDeck
            ViewDecks -.-> ModifyDeck(Modify Existing Deck)
                ModifyDeck --> SelectDeck[Select Deck] -- User Makes Changes --> SaveChanges(Save Changes) --> ViewDecks
    
    AdminHomepage -.-> ViewSubmissions[View Card Submissions] --> Actions{Actions}
        Actions -.-> AddSubmission[Add Submission]:::green
        Actions -.-> RejectSubmission[Reject Submission]:::red 
    
    AdminHomepage -.-> CardManagement[Manage Cardbase]
    CardManagement -.-> AddCard[Add Card] --> SubmitChange[Submit Changes]
    CardManagement -.-> RemoveCard[Remove Card] --> SubmitChange[Submit Changes] --> CardManagement

    
    



    
    
    