Public Class frmRecord
    Private Sub btnRegistrar_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnRegistrar.Click
        txtEdadMeses.Text = Val(txtEdad.Text) * 12
    End Sub
    Private Sub chkFiebre_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkFiebre.CheckedChanged
        txtTemperatura.Visible = True
    End Sub
    Private Sub chkVomitos_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkVomitos.CheckedChanged
        txtEpisodios.Visible = True
    End Sub
    Private Sub chkSangrado_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkSangrado.CheckedChanged
        txtAreas.Visible = True
    End Sub

End Class
