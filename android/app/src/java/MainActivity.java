package com.macrohard.suraj.greelog;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebView;
import android.widget.ShareActionProvider;

import javax.security.auth.Subject;


public class MyActivity extends ActionBarActivity {

    private WebView ourBrowser;
    private ShareActionProvider mShareActionProvider;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);
        ourBrowser = (WebView) findViewById(R.id.wvMainactivity);
        ourBrowser.setWebViewClient(new ViewClient());

        ourBrowser.getSettings().setJavaScriptEnabled(true);
        ourBrowser.getSettings().setLoadWithOverviewMode(true);
        ourBrowser.getSettings().setUseWideViewPort(true);

        ourBrowser.loadUrl("http://greelog.pythonanywhere.com");

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        ourBrowser.goBack();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate menu resource file.
        getMenuInflater().inflate(R.menu.my,menu);
        MenuItem share = menu.findItem(R.id.menu_item_share);
       share.setOnMenuItemClickListener(new MenuItem.OnMenuItemClickListener() {
           @Override
           public boolean onMenuItemClick(MenuItem item) {
               Intent intent=new Intent(android.content.Intent.ACTION_SEND);
               intent.setType("text/plain");
               intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET);
               intent.putExtra(Intent.EXTRA_SUBJECT, "Share message");
               intent.putExtra(Intent.EXTRA_TEXT, "Shared via Greelog");
               startActivity(Intent.createChooser(intent, "Share Via"));
               return true;
           }
       });
        return  true;
    }


}
