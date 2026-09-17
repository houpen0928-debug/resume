(() => {
  const form = document.getElementById('journal-editor');
  if (!form) return;
  const field = id => document.getElementById(id);
  const now = new Date();
  field('post-date').value = [now.getFullYear(), String(now.getMonth()+1).padStart(2,'0'), String(now.getDate()).padStart(2,'0')].join('-');
  const token = Date.now().toString(36);
  function build() {
    const lang = field('post-language').value;
    const values = {layout:'journal', title:field('post-title').value.trim(), date:field('post-date').value, lang, locale:lang, author_profile:true, resume_style:true, description:field('post-summary').value.trim()};
    if (lang === 'en') {values.author='jason_en'; values.site_title='Jason Hung | Plant Operations';}
    const text = '---\n' + Object.entries(values).map(([key,value]) => key + ': ' + JSON.stringify(value)).join('\n') + '\n---\n\n' + field('post-body').value + '\n';
    return {name:values.date+'-'+token+'.md', text};
  }
  function download(post) {
    const url = URL.createObjectURL(new Blob([post.text], {type:'text/markdown;charset=utf-8'}));
    const link = document.createElement('a'); link.href=url; link.download=post.name; link.click();
    setTimeout(() => URL.revokeObjectURL(url),1000);
  }
  field('download-post').addEventListener('click', () => {if(form.reportValidity()) download(build());});
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!field('post-title').value.trim() || !field('post-body').value.trim()) {field('editor-status').textContent='請填入標題與正文 / Enter a title and content.'; return;}
    const post = build();
    const url = new URL('https://github.com/houpen0928-debug/resume/new/codex/resume-executive-0915');
    url.searchParams.set('filename','_journal/'+post.name); url.searchParams.set('value',post.text);
    if (url.href.length > 7000) {
      download(post);
      field('editor-status').textContent='文章較長，已下載 Markdown 檔案。請至「管理／編輯已發布文章」，選 Add file → Upload files 上傳並儲存。 / Long post downloaded. Upload it using Add file → Upload files in Manage published posts.';
      return;
    }
    window.open(url.href,'_blank','noopener,noreferrer');
    field('editor-status').textContent='請在 GitHub 確認內容並按 Commit changes；若未開啟，請允許彈出視窗。 / Review and commit on GitHub. Allow pop-ups if needed.';
  });
})();
