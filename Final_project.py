baker = Turtle() # because we're baking a pie 
baker.penup()
baker.sety(-RADIUS)
baker.pendown()
for _, fraction in letter_frequencies:
        baker.fillcolor(next(COLORS))     
        baker.begin_fill()     
        baker.circle(RADIUS, fraction * 360 / total)     
        position = baker.position()     
        baker.goto(0, 0)     
        baker.end_fill()     
        baker.setposition(position)
