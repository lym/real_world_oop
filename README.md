# Real-world OOP
This project implements card rules in a black jack game. It can be
extended to create blackjack game simulations.

## OOP Ideas
### Inheritance
AceCard, NumberCard and FaceCard inherit from the generic Card class

### Encapsulation
Python is not well suitable for situations were we need strict data
encapsulatio but it is sort of implied by use of methods whose names are
preceded by underscores for example the Deck class' `_gen_numbered_cards()`, and
`_gen_face_cards()` methods.

### Reuse
This is enabled by specifying all the classes in their own modules
(modules) so they can be easily usable in isolation
