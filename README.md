# REST_API_creation_sample

## How to use
#### 1.Run server
```
$ python RESTAPI_example.py
Running server!
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

#### 2. Post {"feature1":1,"feature2":2} with curl 
```
$ curl http://127.0.0.1:5000/ -X POST -H 'Content-Type:application/json' -d '{"feature1":1,"feature2":3}'
{
  "Content-Type": "application/json", 
  "feature1": 1, 
  "feature2": 2, 
  "success": true
}
```
