#1 * a + 2 * b + 5 * c + 10 * (n - (a + b + c)) == m
def count(n, m):
	a = 0;
	b = 0;
	c = 0;
	cnt = 0;
	for a in range(n + 1):
		for b in range(n + 1):
		    for c in range(n + 1):
		    	if n - (a + b + c) >= 0 and 1 * a + 2 * b + 5 * c + 10 * (n - (a + b + c)) == m:
		    		print("There are %d coins of 1 point, %d of 2 points, %d of 5 points, %d of 10 points." %(a, b, c, n - (a + b + c)));
		    		cnt += 1;
	return cnt;

def main():
	print("There are 4 kinds of coins, as of 1 point, 2 points, 5 points, 10 points.");
	print("This programme is going to count all the possibilities in combination of different coins.");
	print("Please enter the amount and the sum value of all the coins: ");
	a = int(input("amout: "));
	b = int(input("value: "));
	num = count(a, b);
	print("There are %d possibilities of all the combination." %num);


if __name__ == "__main__":
	main();


