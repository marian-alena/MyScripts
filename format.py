snack = '{} and {}'.format( 'Burger' , 'Fries' )
print( '\nReplaced:' , snack )

snack = '{1} and {0}'.format( 'Burger' , 'Fries' )
print( 'Replaced:' , snack )

snack = '%s and %s, %.3f' % ( 'Milk' , 'Cookies' , 5.1 )
print( '\nSubstituted:' , snack )