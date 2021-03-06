1)  http://smalleaf.blogspot.com/2011/10/switch-bpdu-guard.html
1.spanning-tree: 中文好像翻成生成樹，管它什麼翻譯，這個東西是Switch上的設定，設定上去後，Switch與Switch之間會相互溝通，避免網路迴圈(loop)狀況產生，缺點是剛接上switch的設備會需要30~50秒的時間…溝通…之後網路才會通。

2.portfast: 這是spanning-tree的進階設定，目的就是當確定網路port所連接的設備確定是終端設備，如印表機、PC、Server等時，不需要switch之間的spanning-tree那30~50秒的溝通，可以利用portfast跳過這個溝通時間。

3.BPDU:全面為bridge protocol data unit，為switch之間spanning-tree溝通的協定資料，只要有spanning-tree的環境就會有BPDU存在。

了解這三個名詞之後，再來看spanning-tree的進階設定"BPDUGUARD"，我們知道bpdu是switch之間溝通spanning-tree的協定資料，那來防止bpdu的bpduguard就是防止switch之間溝通spanning-tree的保彪，問題是…為什麼要禁止spanning-tree呀??這不是防止loop發生的好機制嗎??

原因是spanning-tree是cisco switch預設的功能，只要開機就有啦!!所以只要把一台switch接到另一個swich就會發生spanning-tree的溝通。這時....BPDU GUARD的功就用產生了，可以用來避免人把swich接到自已的網路環境，因為只要一接上就會有bpdu協定資料出現，這時bpdu guard就會將該port error disable，來避免有人私接swich進網路環境。

聰明的您應該有發現，這有個前提，整個bpdu guard的保護只能保護會發送bpdu的switch，如果對方把spanning-tree關掉，或是非cisco swich，這個安全機制就破功啦@@

雖然如此，這還是一個很好的功能，比如說某天自已忘了，接了一台swich上去，更動了原本的STP架構，這不就糗了!!透過BPDU GUARD就是在避免STP被更動的危險狀況!!



2) show spanning-tree inconsistentports
http://cyruslab.net/2012/12/22/cisco-systems-spanning-tree-inconsistent-port/
