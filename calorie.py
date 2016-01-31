
def calorie(W,H,A):
	return 655.096 + 9.563 * W + 1.85 * H - 4.676 * A

def main():
	W = float(input("Enter Weight ( kg):\n"))
	H = float(input("Enter Height ( cm):\n"))
	A = float(input("Enter  Age   (int):\n"))
	print(calorie(W,H,A))

main()