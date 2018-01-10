using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ASPProject
{
    public partial class WebForm1 : System.Web.UI.Page
    {
      
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void SignUp_Click(object sender, EventArgs e)
        {
            Response.Redirect("Registration.aspx");
        }

        
        
        protected void Submit_Click(object sender, EventArgs e)
        {
            LinqtoSQLDataContext datac = new LinqtoSQLDataContext();
            var query = from p in datac.details
                        where p.Fnm == txtName.Text.ToString() && p.pass == Password.Text.ToString()
                        select p;

            if (query.Any())
            {
                Session["UserName"] = txtName.Text;
                Server.Transfer("Profile.aspx");
            }
            else
            {
                Errorlbl.Text = "Invalid Credentials!";
            }

            //HttpCookie cookie = new HttpCookie("LoginInfo");
            //cookie.Value = "Ketan";  
            //Response.Cookies.Add(cookie);
            //Server.Transfer("Profile.aspx");
            ////Response.Redirect("Profile.aspx");
            //String en=TxtEn.Text;
            //Response.Redirect("Profile.aspx?Enroll="+en);
        }

        
    }
}