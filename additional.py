#import logging
from telegram import InlineKeyboardButton
keyboard = [[InlineKeyboardButton("Breakfast", callback_data='Breakfast'),
                InlineKeyboardButton("Lunch", callback_data='Lunch'),
                InlineKeyboardButton("Dinner", callback_data='Dinner'),
                InlineKeyboardButton("Dessert", callback_data='Dessert'),
                InlineKeyboardButton("Drink", callback_data='Drink'),
                InlineKeyboardButton("Salad", callback_data='Salad')]
                ]
keyboard1 = [[InlineKeyboardButton('Omelette', callback_data = 'Omelette')],
                 [InlineKeyboardButton('Mini super-fruit breakfast wraps', callback_data = 'Mini super-fruit breakfast wraps')],
                 [InlineKeyboardButton('One-cup pancakes with blueberries', callback_data = 'One-cup pancakes with blueberries')],
                 [InlineKeyboardButton('Egg & mango chutney flatbreads', callback_data = 'Egg & mango chutney flatbreads')],
                 [InlineKeyboardButton('Silky masala eggs', callback_data = 'Silky masala eggs')],
                 [InlineKeyboardButton('Apple & pecan porridge', callback_data = 'Apple & pecan porridge')],
                 [InlineKeyboardButton('Chocolate porridge', callback_data = 'Chocolate porridge')]
                  ]
keyboard2 = [[InlineKeyboardButton('Pasta', callback_data = 'Pasta')],
                 [InlineKeyboardButton('Carrot soup', callback_data = 'Carrot soup')],
                 [InlineKeyboardButton('Spicy avocado wraps', callback_data = 'Spicy avocado wraps')],
                 [InlineKeyboardButton('Barney-Monday night rice', callback_data = 'Barney-Monday night rice')],
                 [InlineKeyboardButton('Sesame butterflied chicken', callback_data = 'Sesame butterflied chicken')],
                 [InlineKeyboardButton('Smoky veggie chilli', callback_data = 'Smoky veggie chilli')],
                 [InlineKeyboardButton('Chicken gumbo', callback_data = 'Chicken gumbo')]
                  ]
keyboard3 = [[InlineKeyboardButton('Pot-roast beef', callback_data = 'Pot-roast beef')],
                 [InlineKeyboardButton('Moroccan chickpea soup', callback_data = 'Moroccan chickpea soup')],
                 [InlineKeyboardButton('Spanish rice & prawn one-pot', callback_data = 'Spanish rice & prawn one-pot')],
                 [InlineKeyboardButton('Mild chilli & bean pasta bake', callback_data = 'Mild chilli & bean pasta bake')],
                 [InlineKeyboardButton('Super tasty Spanish roast chicken', callback_data = 'Super tasty Spanish roast chicken')],
                 [InlineKeyboardButton('The nicest tray-baked lemon sole', callback_data = 'The nicest tray-baked lemon sole')],
                 [InlineKeyboardButton('Spicy root & lentil casserole', callback_data = 'Spicy root & lentil casserole')]
                  ]
keyboard4 = [[InlineKeyboardButton('Pumpkin pie with pecan crumble', callback_data = 'Pumpkin pie with pecan crumble')],
                 [InlineKeyboardButton('Blackcurrant ombré cheesecake', callback_data = 'Blackcurrant ombré cheesecake')],
                 [InlineKeyboardButton('Almond pastry puff', callback_data = 'Almond pastry puff')],
                 [InlineKeyboardButton('Brigadeiros', callback_data = 'Brigadeiros')],
                 [InlineKeyboardButton('Apple & date pie', callback_data = 'Apple & date pie')],
                 [InlineKeyboardButton('Cherry chocolate mousse', callback_data = 'Cherry chocolate mousse')],
                 [InlineKeyboardButton('Lamingtons', callback_data = 'Lamingtons')]
                  ]
keyboard5 = [[InlineKeyboardButton('Pink pepper negroni', callback_data = 'Pink pepper negroni')],
                 [InlineKeyboardButton('Aperol & grapefruit citrus jellies', callback_data = 'Aperol & grapefruit citrus jellies')],
                 [InlineKeyboardButton('Oat, pear & cardamom smoothie', callback_data = 'Oat, pear & cardamom smoothie')],
                 [InlineKeyboardButton('Limoncello', callback_data = 'Limoncello')],
                 [InlineKeyboardButton('Watermelon glory', callback_data = 'Watermelon glory')],
                 [InlineKeyboardButton('Mint & raspberry julep', callback_data = 'Mint & raspberry julep')],
                 [InlineKeyboardButton('Passion fruit caipirinha', callback_data = 'Passion fruit caipirinha')]
                  ]
keyboard6 = [[InlineKeyboardButton('Roast chicken & crispy bread salad', callback_data = 'Roast chicken & crispy bread salad')],
                 [InlineKeyboardButton('Drunken broad bean & goat’s cheese salad', callback_data = 'Drunken broad bean & goat’s cheese salad')],
                 [InlineKeyboardButton('Hearts of palm & chicken chopped salad', callback_data = 'Hearts of palm & chicken chopped salad')],
                 [InlineKeyboardButton('Sliced fennel, orange & almond salad', callback_data = 'Sliced fennel, orange & almond salad')],
                 [InlineKeyboardButton('Watermelon & feta salad', callback_data = 'Watermelon & feta salad')],
                 [InlineKeyboardButton('Asparagus & halloumi salad', callback_data = 'Asparagus & halloumi salad')],
                 [InlineKeyboardButton('Simple green salad with lemon dressing', callback_data = 'Simple green salad with lemon dressing')]
                  ]

breakfast_meals = [
    "Omelette", "One-cup pancakes with blueberries", "Egg & mango chutney flatbreads", "Apple & pecan porridge", "Mini super-fruit breakfast wraps", "Silky masala eggs","Chocolate porridge"
]
lunch_meals = [
    "Pasta", "Carrot soup", "Spicy avocado wraps", "Barney-Monday night rice", "Chicken gumbo", "Sesame butterflied chicken", "Smoky veggie chilli"
]
dinner_meals = [
    "Pot-roast beef", "Moroccan chickpea soup", "Spanish rice & prawn one-pot", "Mild chilli & bean pasta bake", "Spicy root & lentil casserole", "Super tasty Spanish roast chicken", "The nicest tray-baked lemon sole"
]
dessert_meals = [
    "Pumpkin pie with pecan crumble", "Blackcurrant ombré cheesecake", "Almond pastry puff", "Brigadeiros", "Lamingtons", "Apple & date pie", "Cherry chocolate mousse"
]
drink_meals = [
    "Pink pepper negroni", "Aperol & grapefruit citrus jellies", "Oat, pear & cardamom smoothie", "Limoncello", "Watermelon glory", "Mint & raspberry julep", "Passion fruit caipirinha"
]
salad_meals = [
    "Roast chicken & crispy bread salad", "Drunken broad bean & goat’s cheese salad","Hearts of palm & chicken chopped salad","Sliced fennel, orange & almond salad","Watermelon & feta salad", "Asparagus & halloumi salad", "Simple green salad with lemon dressing"
]