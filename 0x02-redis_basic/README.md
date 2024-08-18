0x02-redis_basic

Understanding method.__self__
The __self__ attribute of a bound method provides access to the instance to which the method is bound.

Here’s how it works:

Bound Method:

When you call obj.method(), Python automatically binds the method to the instance obj. This binding allows you to call the method without explicitly passing the instance as the first argument.
Accessing self:

When you have a bound method (like obj.method), method.__self__ gives you the instance obj to which the method is bound.

self = method.__self__:

This retrieves the instance on which the method was called, allowing access to the Redis client stored in self._redis.
