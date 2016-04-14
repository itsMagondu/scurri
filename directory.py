#The following library accepts data via system args. This however can be reused in a restful API or as a cgi script.
#Sys args were chose for ease of testing
import sys
import re

def match(address):
	if not re.match(r'^(([gG][iI][rR] {0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|'
                        r'(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9]'
                        r'[abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2}))$',address):
		print "Failed. '%s' is NOT a valid postal address" %address
	else:
		print "Success. '%s' is a valid postal address" %address

def test():
	tests = ["M1 1AE",'','12 345','W1A 0AX','W1A A0X','W1A 0AXP','1W1A 0AX','w1A 0ax','QR2 6XH']
	for t in tests:
		match(t)

if __name__ == "__main__":
	try:
		arg = sys.argv[1]
	except:
		print "Please supply a postal address or the word 'test'"
		sys.exit()


	if arg.lower() == 'test':
		test()
	else:
		match(arg)
