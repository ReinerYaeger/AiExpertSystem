male('John')
male('Mark')
female('Kim')
female('Alice')

parent_of('Mark','John')
parent_of('Kim','Alice')


sibling(S1,S2):-parent_of(X,S1),parent_of(X,S2)
