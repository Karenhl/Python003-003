class Open():
    # 开始的时候执行
    def __enter__(self):
        print("open")

    # 最终都要执行
    def __exit__(self, type, value, trace):
        print("close")

    def __call__(self):
        pass

with Open() as f:
    pass