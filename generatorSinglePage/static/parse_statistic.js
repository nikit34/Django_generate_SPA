document.addEventListener('DOMContentLoaded', () => {
    let cut_root_path = window.location.href.split('/');
    let end_root_path = cut_root_path[cut_root_path.length - 2];
    let penult_root_path = cut_root_path[cut_root_path.length - 3];
    let item_localStorage, arr_tr, cut_path;
    if(end_root_path == 'pages'){
        arr_tr = document.getElementsByClassName('slug');
        for(let i = 0; i < arr_tr.length; i++){
            cut_path = arr_tr[i].attributes.value.textContent.split('/');
            end_root_path = cut_path[cut_path.length - 2];
            item_localStorage = localStorage.getItem(end_root_path);
            if(item_localStorage == 'NaN' || item_localStorage == null) {
                document.getElementsByClassName('views')[i].innerHTML = '0';
            } else {
                document.getElementsByClassName('views')[i].innerHTML = item_localStorage;
            }
        }
    }
    else if(penult_root_path == 'page') {
        item_localStorage = localStorage.getItem(end_root_path)
        if(item_localStorage == 'NaN' || item_localStorage == null) {
            document.getElementsByClassName('views')[0].innerHTML = '1';
            localStorage.setItem(end_root_path, 1);
        } else {
            let new_count_views = parseInt(item_localStorage) + 1;
            localStorage.setItem(end_root_path, new_count_views);
            document.getElementsByClassName('views')[0].innerHTML = new_count_views;
        }

        arr_tr = document.getElementsByClassName('slug');
        for(let i = 1; i <= arr_tr.length; i++) {
            cut_path = arr_tr[i - 1].attributes.value.textContent.split('/');
            end_root_path = cut_path[cut_path.length - 2];
            item_localStorage = localStorage.getItem(end_root_path);
            if(item_localStorage == 'NaN' || item_localStorage == null) {
                document.getElementsByClassName('views')[i].innerHTML = '0';
            } else {
                document.getElementsByClassName('views')[i].innerHTML = item_localStorage;
            }
        }
    }
    else if(end_root_path == 'search') {
        arr_tr = document.getElementsByClassName('slug');
        for(let i = 0; i < arr_tr.length; i++){
            cut_path = arr_tr[i].attributes.value.textContent.split('/');
            end_root_path = cut_path[cut_path.length - 2];
            item_localStorage = localStorage.getItem(end_root_path);
            if(item_localStorage == 'NaN' || item_localStorage == null) {
                document.getElementsByClassName('views')[i].innerHTML = '0';
            } else {
                document.getElementsByClassName('views')[i].innerHTML = item_localStorage;
            }
        }
    }

    let star = document.getElementsByClassName('stars')[0];
    if (window.getComputedStyle(star).display !== "none") {
        let sum_views = localStorage.getItem('sum_views');
        if(sum_views == 'NaN'){
            sum_views = 0;
        }
        for(let i = 0; i < localStorage.length; i++) {
            sum_views = parseInt(sum_views) + parseInt(localStorage[localStorage.key(i)]);
            for(let i = 0; i < 5; i++) {
                if (parseInt(sum_views) > i * 40) {
                    document.getElementsByClassName('stars')[i].style.filter = 'grayscale(0%)';
                }
            }
        }
        localStorage.setItem('sum_views', sum_views);
    }
});
