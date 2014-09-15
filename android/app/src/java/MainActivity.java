package com.macrohard.suraj.greelog;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebView;
import android.widget.ShareActionProvider;


public class MainActivity extends Activity {
    WebView ourBrowser;
    private ShareActionProvider mShareActionProvider;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ourBrowser = (WebView) findViewById(R.id.wvMainactivity);
        ourBrowser.setWebViewClient(new ViewClient());

        ourBrowser.getSettings().setJavaScriptEnabled(true);
        ourBrowser.getSettings().setLoadWithOverviewMode(true);
        ourBrowser.getSettings().setUseWideViewPort(true);

        ourBrowser.loadUrl("http://www.greelog.pythonanywhere.com");

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        ourBrowser.goBack();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate menu resource file.
        getMenuInflater().inflate(R.menu.main, menu);

        // Locate MenuItem with ShareActionProvider
        MenuItem item = menu.findItem(R.id.menu_item_share);

        // Fetch and store ShareActionProvider
        mShareActionProvider = (ShareActionProvider) item.getActionProvider();
        Intent shareIntent = new Intent(Intent.ACTION_SEND);
        shareIntent.setAction(Intent.ACTION_SEND);
        shareIntent.setType("text/plain");
        shareIntent.putExtra(Intent.EXTRA_TEXT ,"via GreeLog");
        mShareActionProvider.setShareIntent(shareIntent);

        // Return true to display menu
        return true;
    }


}
