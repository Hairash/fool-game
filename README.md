# fool-game

## Plan
* (User authorization)
* Display name of user, who send the message
* Start game on button click with the players that are connected at the moment
* Send message to everyone in the game
* Receive message and output it (card)


## API
Hearts ♥  
Tiles ♦  
Clovers ♣  
Pikes ♠  

Card: {rank, suit}. Examples: {rank: 6, suit: h}, {rank: Q, suit: c}.

C <-> S message - for test  
C -> S name? - login with the name  
C -> S start - start game  
C <-> S attack - attack with a card {card, attacker}  
C <-> S defend - defend with a card {card, defender}  
C <-> S move - move card to the next player {card, mover}  
C <-> S done - all the cards are biten  
C <-> S take - the defender takes the cards  

