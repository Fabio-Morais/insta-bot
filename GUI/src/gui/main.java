package gui;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JButton;
import javax.swing.LayoutStyle.ComponentPlacement;
import net.miginfocom.swing.MigLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;
import javax.swing.JSeparator;
import java.awt.Color;
import javax.swing.JToolBar;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.Component;
import java.awt.FlowLayout;
import javax.swing.BoxLayout;
import javax.swing.JPopupMenu;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class main {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					main window = new main();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public main() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setResizable(false);
		frame.setBounds(100, 100, 744, 487);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel mid = new JPanel();
		frame.getContentPane().add(mid, BorderLayout.CENTER);
		
		JButton btnNewButton = new JButton("Like");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		
		JButton btnNewButton_1 = new JButton("Comment");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		
		JButton btnFollow = new JButton("Follow");
		btnFollow.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		
		JButton btnNewButton_1_1 = new JButton("Get Names");
		btnNewButton_1_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		
		JButton btnNewButton_1_1_1 = new JButton("Start");
		btnNewButton_1_1_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		GroupLayout gl_mid = new GroupLayout(mid);
		gl_mid.setHorizontalGroup(
			gl_mid.createParallelGroup(Alignment.TRAILING)
				.addGroup(gl_mid.createSequentialGroup()
					.addGap(121)
					.addGroup(gl_mid.createParallelGroup(Alignment.TRAILING)
						.addComponent(btnFollow, GroupLayout.DEFAULT_SIZE, 191, Short.MAX_VALUE)
						.addComponent(btnNewButton, GroupLayout.DEFAULT_SIZE, 191, Short.MAX_VALUE))
					.addGap(84)
					.addGroup(gl_mid.createParallelGroup(Alignment.TRAILING)
						.addComponent(btnNewButton_1_1, GroupLayout.DEFAULT_SIZE, 191, Short.MAX_VALUE)
						.addComponent(btnNewButton_1, GroupLayout.DEFAULT_SIZE, 191, Short.MAX_VALUE))
					.addGap(151))
				.addGroup(Alignment.LEADING, gl_mid.createSequentialGroup()
					.addGap(258)
					.addComponent(btnNewButton_1_1_1, GroupLayout.PREFERRED_SIZE, 191, GroupLayout.PREFERRED_SIZE)
					.addContainerGap(289, Short.MAX_VALUE))
		);
		gl_mid.setVerticalGroup(
			gl_mid.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_mid.createSequentialGroup()
					.addGroup(gl_mid.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_mid.createSequentialGroup()
							.addGap(69)
							.addComponent(btnNewButton, GroupLayout.DEFAULT_SIZE, 72, Short.MAX_VALUE)
							.addGap(0))
						.addGroup(gl_mid.createSequentialGroup()
							.addGap(68)
							.addComponent(btnNewButton_1, GroupLayout.DEFAULT_SIZE, 72, Short.MAX_VALUE)
							.addGap(1)))
					.addGap(18)
					.addGroup(gl_mid.createParallelGroup(Alignment.LEADING)
						.addComponent(btnNewButton_1_1, GroupLayout.PREFERRED_SIZE, 67, GroupLayout.PREFERRED_SIZE)
						.addComponent(btnFollow, GroupLayout.DEFAULT_SIZE, 71, Short.MAX_VALUE))
					.addGap(37)
					.addComponent(btnNewButton_1_1_1, GroupLayout.PREFERRED_SIZE, 67, GroupLayout.PREFERRED_SIZE)
					.addGap(88))
		);
		mid.setLayout(gl_mid);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.setBackground(Color.WHITE);
		frame.setJMenuBar(menuBar);
		
		JMenu mnNewMenu = new JMenu("Create");
		mnNewMenu.setBackground(Color.WHITE);
		menuBar.add(mnNewMenu);
		
		JMenuItem mntmNewMenuItem = new JMenuItem("Create fake accounts");
		mntmNewMenuItem.setBackground(Color.WHITE);
		mnNewMenu.add(mntmNewMenuItem);
		
		JMenu mnNewMenu_1 = new JMenu("Help");
		menuBar.add(mnNewMenu_1);
		
		JPanel menu = new JPanel();
		menu.setBackground(Color.WHITE);
		menuBar.add(menu);
		
		JLabel labelUser = new JLabel("Active user:");
		
		JLabel user = new JLabel("UserExample");
		GroupLayout gl_menu = new GroupLayout(menu);
		gl_menu.setHorizontalGroup(
			gl_menu.createParallelGroup(Alignment.LEADING)
				.addGroup(Alignment.TRAILING, gl_menu.createSequentialGroup()
					.addContainerGap(543, Short.MAX_VALUE)
					.addComponent(labelUser)
					.addGap(18)
					.addComponent(user)
					.addContainerGap())
		);
		gl_menu.setVerticalGroup(
			gl_menu.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_menu.createParallelGroup(Alignment.BASELINE)
					.addComponent(user)
					.addComponent(labelUser))
		);
		menu.setLayout(gl_menu);

	}
	private static void addPopup(Component component, final JPopupMenu popup) {
		component.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			public void mouseReleased(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			private void showMenu(MouseEvent e) {
				popup.show(e.getComponent(), e.getX(), e.getY());
			}
		});
	}
}
