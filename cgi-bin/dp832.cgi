#!/bin/bash
# Remote control rigol dp832 by CGI, H.F. 20201231
# TODO: get past state at the begin
# ref: http://www.yolinux.com/TUTORIALS/BashShellCgi.html

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Rigol DP832 Web Controller</title>'
echo '</head>'
echo '<body>'
  echo "<form method=GET action=\"${SCRIPT}\">"\
       '<table nowrap>'\
          '<tr><td><td>CH1<td><td>CH2<td><td>CH3<td></tr>'\
	  '<tr><td> Voltage(V)</TD>'\
	  '<TD><input type="number" name="ch1_v" min=0 max=30 step=0.001>'\
	  '<td><input type="checkbox" name="ch1_v_s" size=1>'\
	  '<TD><input type="number" name="ch2_v" min=0 max=30 step=0.001>'\
	  '<td><input type="checkbox" name="ch2_v_s" size=1>'\
	  '<TD><input type="number" name="ch3_v" min=0 max=30 step=0.001>'\
	  '<td><input type="checkbox" name="ch3_v_s" size=1>'\
	  '<tr><td> Current(A)'\
	  '<td><input type="number" name="ch1_i" min=0 max=3 step=0.01>'\
	  '<td><input type="checkbox" name="ch1_i_s" size=1>'\
	  '<td><input type="number" name="ch2_i" min=0 max=3 step=0.01>'\
	  '<td><input type="checkbox" name="ch2_i_s" size=1>'\
	  '<td><input type="number" name="ch3_i" min=0 max=3 step=0.01>'\
	  '<td><input type="checkbox" name="ch3_i_s" size=1>'\
	  '<tr><td>State'\
	  '<td><input type="radio" name="ch1" value=1>On'\
	  '<input type="radio" name="ch1" value=0>Off'\
	  '<td><input type="checkbox" name="ch1_s" value="">'\
	  '<td><input type="radio" name="ch2" value=1>On'\
	  '<input type="radio" name="ch2" value=0>Off'\
	  '<td><input type="checkbox" name="ch2_s" value="">'\
	  '<td><input type="radio" name="ch3" value=1>ON'\
	  '<input type="radio" name="ch3" value=0>OFF'\
	  '<td><input type="checkbox" name="ch3_s" value="">'\
       '</table>'
 
  # TODO: print current information
  echo '<br><input type="submit" value="Apply all change">'\
       '<input type="reset" value="Reset"></form>'

  # Make sure we have been invoked properly.

  if [ "$REQUEST_METHOD" != "GET" ]; then
        echo "<hr>Script Error:"\
             "<br>Usage error, cannot complete request, REQUEST_METHOD!=GET."\
             "<br>Check your FORM declaration and be sure to use METHOD=\"GET\".<hr>"
        exit 1
  fi

  # If no search arguments, exit gracefully now.

  if [ -z "$QUERY_STRING" ]; then
        exit 0
  else
     echo "$QUERY_STRING"
     # No looping this time, just extract the data you are looking for with sed:
     #ch1_v=`echo "$QUERY_STRING" | sed -n 's/^.*ch1_v=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
  fi
echo '</body>'
echo '</html>'

exit 0
