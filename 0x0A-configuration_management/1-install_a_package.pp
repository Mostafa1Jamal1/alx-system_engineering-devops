# install flask from pip3 Version 2.1.0

# Werkzeug version 2.1.1 must be installed
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
