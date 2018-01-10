<%@ Page Title="" Language="C#" MasterPageFile="~/Master1.Master" AutoEventWireup="true" CodeBehind="Profile.aspx.cs" Inherits="ASPProject.WebForm3" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <br/>
    <div>
        <asp:Button ID="Logout" runat="server" Text="Logout" class="amber-text btn right" onclick="Logout_Click" style="v">
        </asp:Button>
    </div>
    
            <br>
             &nbsp;&nbsp;
   <h5 class="center-align" style="font-family:Arial">Welcome 
       <asp:Label ID="namelbl" runat="server"></asp:Label>
   </h5>
        

    </br>

       <div class="row ">
       <div class="col m3 l3">
       &nbsp;
       </div>
        <div class="col s12 m6 l6">
          <div class="card teal darken-1">
            <div class="card-content white-text">
                <span class="card-title">
                Enrollment no.:</span>
               <%-- <asp:TextBox ID="Name" runat="server" ontextchanged="Name_TextChanged" 
                    CssClass="Noborder"></asp:TextBox>--%>
                <asp:Label ID="Name1" runat="server"></asp:Label>
                <span class="card-title">
                <br />
                Complaint:</span> 
            &nbsp;<asp:TextBox ID="TextBox1" runat="server" TextMode="MultiLine" CssClass="Noborder">
                </asp:TextBox>
            </div>
            <div class="card-action"> 
              <asp:Button ID="post" runat="server" 
                    Text="post" align="right"  
                    ToolTip="Post your complaint" class=" amber-text teal btn right-aligned" 
                    style="margin-top:-10px;" onclick="post_Click">
              </asp:Button>
                <asp:TextBox ID="accept" runat="server" Visible="False" AutoPostBack=true></asp:TextBox>
            </div>
          </div>
        </div>
      </div>
   
</asp:Content>
