
//package project;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javax.swing.JOptionPane;
import static javafx.application.Platform.exit;


/**
 * @author Efrat Weiskopf
 */

    public class ProjectController {
        int rect_height,rect_length, tri_height,tri_length;
        String height, length;

        @FXML
        private TextArea txt_astreisks;


        @FXML
        void btn1(ActionEvent event) {
            String  number,txt="";
            int choosen_num;
            height = JOptionPane.showInputDialog("Enter Height");
            tri_height = Integer.parseInt(height);
            if(tri_height<=0)
                JOptionPane.showMessageDialog(null, "incorrect height", "Error",
                        JOptionPane.ERROR_MESSAGE);
            length = JOptionPane.showInputDialog("Enter width");
            tri_length = Integer.parseInt(length);
            if(tri_length<=0)
                JOptionPane.showMessageDialog(null, "incorrect width", "Error",
                        JOptionPane.ERROR_MESSAGE);
            number = JOptionPane.showInputDialog("Enter 1 to calculate the scope or enter 2 to print ");
            choosen_num = Integer.parseInt(number);
            if(choosen_num==1)
            {
                double tri_scope=2*Math.sqrt(Math.pow(tri_length/2,2)+Math.pow(tri_height,2))+tri_length;
                JOptionPane.showMessageDialog(null, "The scope is:" +tri_scope);
            }
            if(choosen_num==2)
            {
                if ((tri_length % 2 == 0) || (tri_length > (tri_height * 2)))
                    JOptionPane.showMessageDialog(null, "Cannot print the triangle", "Error",
                            JOptionPane.ERROR_MESSAGE);
                else
                {
                    int asterisks = 1;
                    int spaces = tri_length / 2;
                    int x = tri_length / 2 + 1;
                    int i = 1,counter=1;
                    while (i <= tri_height)
                    {
                        for (int j = 1; j <= spaces; j++) {
                            txt+=" ";
                        }
                        for (int j = 1; j <= asterisks; j++) {
                            txt+="*";
                        }
                        txt+="\n";
                        if(tri_height-2==0)
                        {
                            i++;
                            spaces--;
                            asterisks+=2;
                            txt_astreisks.setText(txt);
                            continue;
                        }
                        int division= (tri_height - 2) / (x - 2);
                        int remain = (tri_height - 2) % (x - 2);
                        if (i == 2 && asterisks > 1 && asterisks < tri_length)
                        {
                            counter = division + remain - 1;
                            i+=counter;
                            while (counter > 0)
                            {
                                for (int j = 1; j <= spaces; j++) {
                                    txt+=" ";
                                }
                                for (int j = 1; j <= asterisks; j++) {
                                    txt+="*";
                                }
                                txt+="\n";
                                counter--;
                            }
                            spaces--;
                            asterisks += 2;
                            continue;

                        }
                        if (i != 2 && asterisks > 1 && asterisks < tri_length)
                        {
                            counter= division - 1;
                            i+=counter;
                            while (counter != 0)
                            {
                                for (int j = 1; j <= spaces; j++) {
                                    txt+=" ";
                                }
                                for (int j = 1; j <= asterisks; j++) {
                                    txt+="*";
                                }
                                txt+="\n";
                                counter--;
                            }
                        }

                        spaces--;
                        asterisks += 2;
                        if(asterisks>tri_length)
                        {
                            txt_astreisks.setText(txt);
                            break;

                        }
                        i++;
                    }
                }
            }
            if(choosen_num!=1&&choosen_num!=2)
                JOptionPane.showMessageDialog(null, "Bad Input", "Error",JOptionPane.ERROR_MESSAGE);

        }

        @FXML
        void btn2(ActionEvent event) {
            height = JOptionPane.showInputDialog("Enter height");
            rect_height = Integer.parseInt(height);
            if(rect_height<=0)
                JOptionPane.showMessageDialog(null, "incorrect height", "Error",
                        JOptionPane.ERROR_MESSAGE);
            length = JOptionPane.showInputDialog("Enter length");
            rect_length = Integer.parseInt(length);
            if(rect_height<=0)
                JOptionPane.showMessageDialog(null, "incorrect width", "Error",
                        JOptionPane.ERROR_MESSAGE);
            if(Math.abs(rect_height-rect_length)>5)
                JOptionPane.showMessageDialog(null, "The area of the rectangle is:" +rect_length*rect_height);
            else
            {
                int scope=rect_length*2+rect_height*2;
                JOptionPane.showMessageDialog(null, "The Scope of the rectangle is:" +scope);

            }
        }

        @FXML
        void btn3(ActionEvent event) {
            exit();
        }


    }

