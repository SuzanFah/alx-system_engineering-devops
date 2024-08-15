from graphviz import Digraph

dot = Digraph(comment='Debugging Process for Apache 500 Error')

# Nodes with colors
dot.node('A', '500 Internal Server Error Detected', style='filled', color='red')
dot.node('B', 'Check Apache Error Logs', style='filled', color='orange')
dot.node('C', 'Identify Error in wp-settings.php', style='filled', color='yellow')
dot.node('D', 'Modify wp-settings.php', style='filled', color='green')
dot.node('E', 'Restart Apache Server', style='filled', color='lightblue')
dot.node('F', 'Check Website and Logs', style='filled', color='purple')

# Edges with colors
dot.edge('A', 'B', color='red')
dot.edge('B', 'C', color='orange')
dot.edge('C', 'D', color='yellow')
dot.edge('D', 'E', color='green')
dot.edge('E', 'F', color='blue')

# Save and render
dot.render('debugging_process_apache_500_error', format='png')
