from src.sliding_window_cache import SlidingWindowCache

cache = SlidingWindowCache(3)

print(cache.buff)
cache.add(13,"nikhat")
print(cache.buff)
cache.add("shika" ,"raj")
print(cache.buff)
cache.add("mango", 15)
print(cache.buff)
print(list(cache.get_recent_windows(2)))
print(list(cache.get_recent_windows(2,reverse=True)))
