/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Date;

import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import java.awt.BorderLayout;

import java.awt.Image;
import java.time.LocalDate;
import javax.swing.ImageIcon;
import java.awt.Dimension;
import javax.swing.BoxLayout;
import java.awt.Component;
import java.awt.GridLayout;

/**
 *
 * @author death
 */
public class DashboardForm extends javax.swing.JFrame {
    
    private int currentMovieId;
    private int currentUserId;

    /**
     * Creates new form DashboardForm
     */
    public DashboardForm(int userId) {
                
        this.currentUserId = userId;
        
        setTitle("Mana Movie Rental System");

        initComponents();
        
        
        // Filters - START 
        comboGenreFilter.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] {"All", "Sci-Fi", "Animation", "Action", "Fantasy", "Horror", "Thriller"}));
        
        comboGenreFilter.addActionListener(new java.awt.event.ActionListener() { 
            
            public void actionPerformed(java.awt.event.ActionEvent evt) {
            
                
                loadMovies(); 
            
            }
        
        });
        
        // Filters - END 

        System.out.println("Loading movies...");
        loadMovies(); 
        
    }
    
    
    // START - loadMovies
    private void loadMovies(){

        try (Connection conn = DBConnection.connect()) {
          String selectedGenre = comboGenreFilter.getSelectedItem().toString();
          String sql;

          if (selectedGenre.equals("All")) {
              
              sql = "SELECT * FROM Movies";
              
          } else {
              
              sql = "SELECT * FROM Movies WHERE genre = ?";
              
          }

          PreparedStatement stmt = conn.prepareStatement(sql);

          if (!selectedGenre.equals("All")) {
              
              stmt.setString(1, selectedGenre);
              
          }

          ResultSet rs = stmt.executeQuery();

          panelMovies.removeAll();
          panelMovies.setLayout(new GridLayout(0, 2, 10, 10)); 

          while (rs.next()) {
              
              int id = rs.getInt("id");
              String title = rs.getString("title");
              String imagePath = rs.getString("poster_path");

              JPanel card = new JPanel();
              card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));

              JLabel lblTitle = new JLabel(title, JLabel.CENTER);
              lblTitle.setAlignmentX(Component.CENTER_ALIGNMENT);

              JLabel lblImage = new JLabel();
              lblImage.setAlignmentX(Component.CENTER_ALIGNMENT);

              try {

                  ImageIcon icon = new ImageIcon(getClass().getResource("/images/" + imagePath));
                  Image image = icon.getImage().getScaledInstance(120, 180, Image.SCALE_SMOOTH);
                  lblImage.setIcon(new ImageIcon(image));

              } catch (Exception ex) {

                  lblImage.setText("No image found.");
                  ex.printStackTrace();

              }

              JButton btnDetails = new JButton("Details");
              btnDetails.setAlignmentX(Component.CENTER_ALIGNMENT);
              btnDetails.addActionListener(e -> loadMovieDetails(id));

              card.add(lblTitle);
              card.add(lblImage);
              card.add(btnDetails);

              panelMovies.add(card);

          }

          panelMovies.revalidate();
          panelMovies.repaint();

        } catch (Exception e) {

          e.printStackTrace();

        }
       

    }
        // END - loadMovies
    
    //START - loadMovieDetails 
    private void loadMovieDetails(int movieId){
        
        try (Connection conn = DBConnection.connect()){
            
            String sql = "SELECT * FROM Movies WHERE id = ?"; 
            PreparedStatement stmt = conn.prepareStatement(sql); 
            stmt.setInt(1, movieId);
            ResultSet rs = stmt.executeQuery();
            
            currentMovieId = movieId;
            
            if (rs.next()) {
                txtTitle.setText(rs.getString("title"));
                txtDirector.setText(rs.getString("director"));
                txtWriters.setText(rs.getString("writers"));
                txtReleaseDate.setText(rs.getString("release_date"));
                txtRunningTime.setText(rs.getString("duration"));
                txtRated.setText(rs.getString("rating"));
                txtGenre.setText(rs.getString("genre"));
                txtCast.setText(rs.getString("cast"));
                
                try {
                    
                    ImageIcon icon = new ImageIcon(getClass().getResource("/images/" + rs.getString("poster_path")));
                    Image image = icon.getImage().getScaledInstance(140, 180, Image.SCALE_SMOOTH);
                    lblPoster.setIcon(new ImageIcon(image)); 
                   
                } catch (Exception ex) {
                    lblPoster.setText("No image found.");
                    ex.printStackTrace();
                }

            }
            
            
            String unitCheckSql = "SELECT dvd_units, blu_ray_units FROM Movies WHERE id = ?"; 
            PreparedStatement unitStmt = conn.prepareStatement(unitCheckSql); 
            unitStmt.setInt(1, movieId);
            ResultSet unitRs = unitStmt.executeQuery();
            
            if (unitRs.next()) {
                
                int dvdUnits = unitRs.getInt("dvd_units"); 
                int bluRayUnits = unitRs.getInt("blu_ray_units"); 
                
                if (dvdUnits <= 0) {
                    
                    btnHoldDVD.setEnabled(false);
                    btnHoldDVD.setText("Currently Unavailable"); 
                    
                } else {
                    
                    btnHoldDVD.setEnabled(true);
                    btnHoldDVD.setText("Hold DVD");
                    
                }
                
                if (bluRayUnits <= 0) {
                    
                    btnHoldBluray.setEnabled(false); 
                    btnHoldBluray.setText("Currently Unavailable");
                    
                } else {
                    
                    btnHoldBluray.setEnabled(true);
                    btnHoldBluray.setText("Hold Blu-Ray");
                    
                }
                
                
            }
            

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
   // END - loadMovies

    private void makeReservation(String format) {

               try (Connection conn = DBConnection.connect()) {
                   
                   String unitColumn = format.equalsIgnoreCase("DVD") ? "dvd_units" : "blu_ray_units"; 
                   String checkSql = "SELECT " + unitColumn + " FROM Movies WHERE id = ?"; 
                   PreparedStatement checkStmt = conn.prepareStatement(checkSql); 
                   checkStmt.setInt(1, currentMovieId); 
                   ResultSet checkRs = checkStmt.executeQuery(); 
                   
                   if (checkRs.next()) {
                       
                       int availableUnits = checkRs.getInt(1); 
                       
                       if (availableUnits <= 0) {
                           
                           JOptionPane.showMessageDialog(this, "Sorry, there are no " + format + " units available for rent at this time.");
                           return;
                           
                       }
                       
                   }
                   
                   
                   
                   String sql = "SELECT title, price_per_day FROM Movies WHERE id = ?";
                   PreparedStatement stmt = conn.prepareStatement(sql);
                   stmt.setInt(1, currentMovieId);
                   ResultSet rs = stmt.executeQuery();

                   if (rs.next()) {
                       String title = rs.getString("title");
                       double pricePerDay = rs.getDouble("price_per_day");
                       LocalDate today = LocalDate.now();
                       LocalDate returnDate = today.plusDays(3);
                       double additionalFees = 0.00;

                       String msg = String.format(
                           "Title: %s\nFormat: %s\nPrice per Day: $%.2f\nReservation Date: %s\nReturn Date: %s\nAdditional Fees: $%.2f",
                           title, format, pricePerDay, today, returnDate, additionalFees
                       );

                       int confirm = JOptionPane.showConfirmDialog(this, msg, "Confirm Reservation", JOptionPane.OK_CANCEL_OPTION);

                       if (confirm == JOptionPane.OK_OPTION) {
                           String insert = "INSERT INTO Reservations (user_id, movie_id, reservation_date, format) VALUES (?, ?, ?, ?)";
                           PreparedStatement insertStmt = conn.prepareStatement(insert);
                           insertStmt.setInt(1, currentUserId);
                           insertStmt.setInt(2, currentMovieId);
                           insertStmt.setDate(3, java.sql.Date.valueOf(today));
                           insertStmt.setString(4, format);
                           insertStmt.executeUpdate();

                           JOptionPane.showMessageDialog(this, "Reservation Confirmed!");
                       }
                   }

               } catch (Exception ex) {
                   ex.printStackTrace();
                   JOptionPane.showMessageDialog(this, "Error: " + ex.getMessage());
               }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jSplitPane1 = new javax.swing.JSplitPane();
        panelMovies = new javax.swing.JPanel();
        panelDetails = new javax.swing.JPanel();
        comboGenreFilter = new javax.swing.JComboBox<>();
        jLabel = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        txtTitle = new javax.swing.JTextField();
        txtDirector = new javax.swing.JTextField();
        txtWriters = new javax.swing.JTextField();
        txtReleaseDate = new javax.swing.JTextField();
        txtRunningTime = new javax.swing.JTextField();
        txtRated = new javax.swing.JTextField();
        txtGenre = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        txtCast = new javax.swing.JTextArea();
        lblPoster = new javax.swing.JLabel();
        btnHoldDVD = new javax.swing.JButton();
        btnHoldBluray = new javax.swing.JButton();
        jLabel1 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        panelMovies.setLayout(new java.awt.GridLayout(0, 2, 10, 10));
        jSplitPane1.setLeftComponent(panelMovies);

        comboGenreFilter.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        comboGenreFilter.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                comboGenreFilterActionPerformed(evt);
            }
        });

        jLabel.setText("Title:");

        jLabel2.setText("Director:");

        jLabel3.setText("Writers:");

        jLabel4.setText("Release Date:");
        jLabel4.setToolTipText("");

        jLabel5.setText("Running Time:");

        jLabel6.setText("Rated:");

        jLabel7.setText("Genre:");

        jLabel8.setText("Cast:");

        txtCast.setColumns(20);
        txtCast.setRows(5);
        jScrollPane1.setViewportView(txtCast);

        lblPoster.setText("Movie Poster");

        btnHoldDVD.setText("Hold DVD");
        btnHoldDVD.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnHoldDVDActionPerformed(evt);
            }
        });

        btnHoldBluray.setText("Hold Blu-Ray");
        btnHoldBluray.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnHoldBlurayActionPerformed(evt);
            }
        });

        jLabel1.setText("Movie Details");

        jLabel9.setText("Reserve for Pickup:");

        javax.swing.GroupLayout panelDetailsLayout = new javax.swing.GroupLayout(panelDetails);
        panelDetails.setLayout(panelDetailsLayout);
        panelDetailsLayout.setHorizontalGroup(
            panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(panelDetailsLayout.createSequentialGroup()
                .addGap(42, 42, 42)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(panelDetailsLayout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(panelDetailsLayout.createSequentialGroup()
                        .addComponent(lblPoster, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(panelDetailsLayout.createSequentialGroup()
                                .addGap(32, 32, 32)
                                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(jLabel2)
                                    .addComponent(jLabel3)
                                    .addComponent(jLabel))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtDirector, javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(txtWriters)
                                    .addComponent(txtTitle)))
                            .addGroup(panelDetailsLayout.createSequentialGroup()
                                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                        .addComponent(jLabel5)
                                        .addComponent(jLabel6, javax.swing.GroupLayout.Alignment.TRAILING)
                                        .addComponent(jLabel7, javax.swing.GroupLayout.Alignment.TRAILING)
                                        .addComponent(jLabel8, javax.swing.GroupLayout.Alignment.TRAILING))
                                    .addGroup(panelDetailsLayout.createSequentialGroup()
                                        .addGap(6, 6, 6)
                                        .addComponent(jLabel4)))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtGenre)
                                    .addComponent(txtRunningTime)
                                    .addComponent(txtReleaseDate, javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addGroup(panelDetailsLayout.createSequentialGroup()
                                        .addComponent(txtRated, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(0, 0, Short.MAX_VALUE))
                                    .addComponent(jScrollPane1)))
                            .addGroup(panelDetailsLayout.createSequentialGroup()
                                .addGap(43, 43, 43)
                                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel9)
                                    .addGroup(panelDetailsLayout.createSequentialGroup()
                                        .addComponent(btnHoldDVD, javax.swing.GroupLayout.PREFERRED_SIZE, 153, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                        .addComponent(btnHoldBluray, javax.swing.GroupLayout.PREFERRED_SIZE, 153, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                .addGap(0, 0, Short.MAX_VALUE)))
                        .addGap(36, 36, 36))))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelDetailsLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(comboGenreFilter, javax.swing.GroupLayout.PREFERRED_SIZE, 129, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(721, 721, 721))
        );
        panelDetailsLayout.setVerticalGroup(
            panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(panelDetailsLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(comboGenreFilter, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(13, 13, 13)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(panelDetailsLayout.createSequentialGroup()
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel)
                            .addComponent(txtTitle, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel2)
                            .addComponent(txtDirector, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel3)
                            .addComponent(txtWriters, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel4)
                            .addComponent(txtReleaseDate, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel5)
                            .addComponent(txtRunningTime, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelDetailsLayout.createSequentialGroup()
                        .addGap(3, 3, 3)
                        .addComponent(lblPoster, javax.swing.GroupLayout.PREFERRED_SIZE, 179, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(txtRated, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(txtGenre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel8)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel9)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(panelDetailsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnHoldBluray, javax.swing.GroupLayout.PREFERRED_SIZE, 46, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnHoldDVD, javax.swing.GroupLayout.PREFERRED_SIZE, 46, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(103, 103, 103))
        );

        jSplitPane1.setRightComponent(panelDetails);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jSplitPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 839, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(31, 31, 31))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jSplitPane1)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    // START - HOLD DVD 
    private void btnHoldDVDActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnHoldDVDActionPerformed
        // TODO add your handling code here:
        makeReservation("DVD");
       
    }//GEN-LAST:event_btnHoldDVDActionPerformed
    // END - HOLD DVD 
    
    
    // START - HOLD BLURAY
    private void btnHoldBlurayActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnHoldBlurayActionPerformed
        // TODO add your handling code here:
        makeReservation("Blu-Ray");

    }//GEN-LAST:event_btnHoldBlurayActionPerformed

    private void comboGenreFilterActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_comboGenreFilterActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_comboGenreFilterActionPerformed
    // END - HOLD BLURAY

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(DashboardForm.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(DashboardForm.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(DashboardForm.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(DashboardForm.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
            new DashboardForm(1).setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnHoldBluray;
    private javax.swing.JButton btnHoldDVD;
    private javax.swing.JComboBox<String> comboGenreFilter;
    private javax.swing.JLabel jLabel;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JSplitPane jSplitPane1;
    private javax.swing.JLabel lblPoster;
    private javax.swing.JPanel panelDetails;
    private javax.swing.JPanel panelMovies;
    private javax.swing.JTextArea txtCast;
    private javax.swing.JTextField txtDirector;
    private javax.swing.JTextField txtGenre;
    private javax.swing.JTextField txtRated;
    private javax.swing.JTextField txtReleaseDate;
    private javax.swing.JTextField txtRunningTime;
    private javax.swing.JTextField txtTitle;
    private javax.swing.JTextField txtWriters;
    // End of variables declaration//GEN-END:variables

}

