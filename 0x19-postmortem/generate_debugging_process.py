from graphviz import Digraph

dot = Digraph(comment='Debugging Process for Apache 500 Error')

# Nodes
dot.node('A', '500 Internal Server Error Detected')
dot.node('B', 'Check Apache Error Logs')
dot.node('C', 'Identify Error in wp-settings.php')
dot.node('D', 'Modify wp-settings.php')
dot.node('E', 'Restart Apache Server')
dot.node('F', 'Check Website and Logs')

# Edges
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

# Save and render
dot.render('debugging_process_apache_500_error', format='png')
