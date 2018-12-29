# PythonChallenge Level4

## About
You need to use urllib2 module to solve this problem.

## LEVEL 2
![chainsaw.jpg](./chainsaw.jpg)

## How to solve
Look at the page source.
```
<html>
<head>
  <title>follow the chain</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
end. 400 times is more than enough. -->
<center>
<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>
<br><br><font color="gold"></center>
Solutions to previous levels: <a href="http://wiki.pythonchallenge.com/"/>Python Challenge wiki</a>.
<br><br>
IRC: irc.freenode.net #pythonchallenge
</body>
</html>
```

If you click image on site, you'll see this sentence.

**and the next nothing is 44827**.

and the url is **http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345**.

so you need to change last number 400 times.

if you execute which i made , you'll see like this.
```
and the next nothing is 17547
and the next nothing is 71456
and the next nothing is 60015
and the next nothing is 38279
and the next nothing is 63928
and the next nothing is 21753
...
...
...
and the next nothing is 96791
and the next nothing is 75635
and the next nothing is 52899
and the next nothing is 66831
peak.html
```

http://www.pythonchallenge.com/pc/def/peak.html
