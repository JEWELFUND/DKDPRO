
if __name__ == "__main__":
        try:
                __import__("DKD").login()
        except Exception as e:
                exit(str(e))
