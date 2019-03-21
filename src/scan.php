<?php

$command = escapeshellcmd('python3 python/main.py');
$output = shell_exec($command);
echo $output;

?>
