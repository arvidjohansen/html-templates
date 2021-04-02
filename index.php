<?PHP
  // output file list in HTML TABLE format
  echo "<table border=\"1\">\n";
  echo "<thead>\n";
  echo "<tr><th>Name</th><th>Type</th><th>Size</th><th>Last Modified</th></tr>\n";
  echo "</thead>\n";
  echo "<tbody>\n";
  foreach($dirlist as $file) {
    echo "<tr>\n";
    echo "<td>{$file['name']}</td>\n";
    echo "<td>{$file['type']}</td>\n";
    echo "<td>{$file['size']}</td>\n";
    echo "<td>",date('r', $file['lastmod']),"</td>\n";
    echo "</tr>\n";
  }
  echo "</tbody>\n";
  echo "</table>\n\n";
?>