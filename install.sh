#!/bin/bash
# Installation script for md2pdf

set -e

echo "Installing md2pdf..."

# Install the package
pip install -e .

# Create ~/bin directory if it doesn't exist
mkdir -p ~/bin

# Create a wrapper script in ~/bin
cat > ~/bin/md2pdf << 'EOF'
#!/bin/bash
# md2pdf wrapper script

python -m md2pdf "$@"
EOF

# Make the wrapper executable
chmod +x ~/bin/md2pdf

echo ""
echo "Installation complete!"
echo ""
echo "md2pdf has been installed to ~/bin/md2pdf"
echo ""
echo "To use md2pdf from anywhere, make sure ~/bin is in your PATH."
echo "Add the following line to your ~/.bashrc or ~/.zshrc if it's not already there:"
echo ""
echo '    export PATH="$HOME/bin:$PATH"'
echo ""
echo "Then reload your shell configuration:"
echo "    source ~/.bashrc   # for bash"
echo "    source ~/.zshrc    # for zsh"
echo ""
echo "Usage: md2pdf <input.md> [-o output.pdf]"
