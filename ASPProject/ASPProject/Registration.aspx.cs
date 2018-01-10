using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ASPProject
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        LinqtoSQLDataContext datac = new LinqtoSQLDataContext();
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void Submit_Click(object sender, EventArgs e)
        {

            if (Page.IsValid)
            {
                Label1.ForeColor = System.Drawing.Color.Green;
                Label1.Text = "Data saved successfully";
                //The database code goes here
                detail dt = new detail
                {
                    Fnm = Fname.Text.ToString(),
                    lnm = Lname.Text.ToString(),
                    eno = rno.Text.ToString(),
                    mob = telephone.Text.ToString(),
                    email = Mail.Text.ToString(),
                    pass = Pass.Text.ToString(),
                };
                datac.details.InsertOnSubmit(dt);
                try
                {
                    datac.SubmitChanges();
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    datac.SubmitChanges();
                }
                
            }
            else
            {

                Label1.ForeColor = System.Drawing.Color.Red;
                Label1.Text = "Error! Data not saved";
            }
           
        }
    }
}